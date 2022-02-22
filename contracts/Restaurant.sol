// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;
pragma experimental ABIEncoderV2;

contract Restaurant {
    address payable owner;
    uint256 ownerFund;
    uint256 menuCount;
    string[] public menus;
    mapping(string => Menu) public nameToMenus;

    constructor() public {
        owner = msg.sender;
        ownerFund = 0;
    }

    modifier onlyOwner() {
        require(owner == msg.sender, "Only the owner is allowed");
        _;
    }

    struct Menu {
        string menuName;
        uint256 menuPrice;
        address owner;
        bool purchased;
    }

    function getOwnerFund() public view onlyOwner returns (uint256) {
        return ownerFund;
    }

    function addMenu(string memory _name, uint256 _price) public onlyOwner {
        nameToMenus[_name] = Menu(_name, _price, owner, false);
        menus.push(_name);
        menuCount++;
    }

    function buyMenu(string memory _name) public payable {
        require(msg.sender != owner, "The owner can't buy food");
        require(msg.value >= nameToMenus[_name].menuPrice, "Not enaough ETH");
        require(
            nameToMenus[_name].purchased == false,
            "Sorry the food has been purchased"
        );
        nameToMenus[_name].owner = msg.sender;
        nameToMenus[_name].purchased = true;
        owner.transfer(msg.value);
        ownerFund += msg.value;
    }

    function retrieveMenu(string memory _name)
        public
        view
        returns (string memory menuName, uint256 menuPrice)
    {
        menuName = nameToMenus[_name].menuName;
        menuPrice = nameToMenus[_name].menuPrice;
    }

    function retrieveAllMenu() public view returns (string[] memory) {
        return menus;
    }

    function getMenuCount() public view returns (uint256) {
        return menuCount;
    }
}

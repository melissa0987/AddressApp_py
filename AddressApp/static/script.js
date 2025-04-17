// bugs: flash messages


window.addEventListener("DOMContentLoaded", function() {

    //variables
    const addressList = document.getElementById('addressList');
    const ul = document.createElement('ul');
    const addButton = document.getElementById("addButton");
    const searchButton = document.getElementById("searchButton");
    
    const searchResult = document.getElementById("searchResult");
    const result = document.getElementById("result");

    addButton.addEventListener("click", addNewAddress);
    searchButton.addEventListener("click", searchAddress);

    // Display all addresses on page load
    getAddresses();
    function getAddresses(){
        
        fetch('/api/addressbook/')
        .then(response => response.json())
        .then(addresses => {
            addresses.forEach(address => {
                const list = document.createElement('li');
                const text = `${address.name}: ${address.street}, ${address.city}, ${address.province}`;
                list.textContent = text;
                ul.appendChild(list);
            });
            addressList.appendChild(ul);
        })
        .catch(error => console.error(`Failed to get addresses: ${error}`));
    }

    //function for searchbutton
    function searchAddress(){
        const searchInput = document.getElementById("searchInput").value;
        if (!searchInput) {
            alert("Search input is empty");
            return;
        }else{
    
            fetch(`api/addressbook/?name=${searchInput}`)
            .then((response) => response.json())
            .then((response) => searchResultDisplay(response))
            .catch(error => console.error(`Something went wrong ${error}`));
        }

    }
    //diaplsys the results 
    function searchResultDisplay(response){

        let name = document.createElement('p');
        let street = document.createElement('p');
        let city = document.createElement('p');
        let province = document.createElement('p');

        let nameText = `Name: ${response.name}`;
        let streetText = `Street: ${response.street},`;
        let cityText = `City: ${response.city},`;
        let provText = `Province: ${response.province}`;

        
        name.textContent = nameText;
        street.textContent = streetText;
        city.textContent = cityText;
        province.textContent = provText;

        //to erase the previous search result
        while (result.firstChild) {
            result.removeChild(result.firstChild);
        }
        result.appendChild(name);
        result.appendChild(street);
        result.appendChild(city);
        result.appendChild(province);

        
        searchResult.appendChild(result);
        
        //TODO bug flash message not working when displaying result that has no match
    }

      //method to add new address
    function addNewAddress(){
        address = {
            "name" : "Dirk",
            "street" : "123 Maple",
            "city" : "Montreal",
            "province" : "Quebec"
        };
        //TODO BUG FIX: flash only appears when after refresh
        
        fetch("api/addressbook/",{
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json' 
            },
            method: "POST",
            body: JSON.stringify(address)
        })
        .then((response) => response.json())
        .catch(error => console.error(`Something went wrong: ${error}`));
    }

}, false);



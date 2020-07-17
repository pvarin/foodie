function add_item(){
    // Locate the list and corresponding items.
    var dynamic_list = document.getElementById("dynamic_list");
    var list_items = dynamic_list.querySelectorAll(".dynamic-list-item");
    var num_elements = list_items.length;

    // Create the new element.
    var new_element = list_items[0].cloneNode(true);
    var id = num_elements+1
    new_element.setAttribute("id", "dynamic_list_item_"+id);
    new_element.querySelectorAll("input").forEach(element => {element.value=""});

    // Insert is after the last element.
    dynamic_list.insertBefore(new_element, list_items[list_items.length-1].nextSibling);
}

function remove_item(event){
    // Get the target: https://stackoverflow.com/questions/1553661/how-to-get-the-onclick-calling-object
    event = event || window.event;
    var target_element = event.target || event.srcElement || event;
    if (target_element.nodeType == 3) target_element = target_element.parentNode; // defeat Safari bug
    
    var dynamic_list = document.getElementById("dynamic_list");
    var list_items = dynamic_list.querySelectorAll(".dynamic-list-item");
    if (list_items.length > 1){
        target_element.parentNode.parentNode.remove();
    }else{
        target_element.parentNode.parentNode.querySelectorAll("input").forEach(element => {element.value=""});
    }
}


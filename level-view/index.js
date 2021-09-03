// hi :)

// Prologue, misc tools i might use and consts:

const level_select = document.getElementById("levelselect");
const explorer = document.getElementById("explorer")

const keyOrder = ["name","music","ambiance","palette"]
// TO DO INDIVIDUALLY AS THEIR OWN THING: exits, objects, decos
// NOT SURE WHAT THIS IS (look into it): 
//  object_id - no clue
//  foley - something to do with foley (no shit)
//  transition - music transitioning?
const exitDir = ["right","top","left","bottom"];
const levelComments = {"1_-1_2":"Unused Luncheon House","1_-1_3":"Unused Pumpernickel House","1_1_2":"Unused Pickle House","1_1_1":"Unused Pea and Ginger House"}


var level = "NA"

// Chapter 1, loading level data:

level_data = {};

document.getElementById('file').onchange = function(){ // level_data loaded
    var file = this.files[0];
    var reader = new FileReader();
    reader.onload = function(progressEvent){
        level_data = JSON.parse(this.result);
        load_levels();
    };
    reader.readAsText(file);
};

function load_levels() {
    level_select.innerHTML = "";
    var level_element = document.createElement("option");
    level_element.value = "NA";
    level_element.innerHTML = "No Option";
    level_select.appendChild(level_element);
    var sortedKeys = Object.keys(level_data).sort();
    for (var level in sortedKeys) {
        level = sortedKeys[level]
        var level_element = document.createElement("option");
        level_element.value = level;
        if (level_data[level]["name"] != level) {
            level_element.innerHTML = level + " - " + level_data[level]["name"];
        } else {
            level_element.innerHTML = level;
        }
        level_select.appendChild(level_element);
    }
}


// Chapter 2, selecting and viewing levels:

level_select.onchange = function(){ // Selected level changed.
    level = level_select.value;
    explorer.innerHTML = "";
    if (level == "NA") {return}
    if (levelComments.hasOwnProperty(level)) {
        var p = document.createElement("p");
        p.innerHTML = "Jdavis' Comment: "+levelComments[level];
        explorer.appendChild(p);
    }
    for (var key in keyOrder) { // Part 1, simple values
        key = keyOrder[key];
        var p = document.createElement("p");
        var input = document.createElement("input");
        p.innerHTML = key + ": ";
        input.value = level_data[level][key];
        p.appendChild(input)
        explorer.appendChild(p);
    }
    var exits = document.createElement("p");
    exits.innerHTML = "exits: "
    for (let i=0;i<4;i++) { // Part 2, exits
        var tickbox = document.createElement("input");
        tickbox.type = "checkbox";
        tickbox.name = "exit"+exitDir[i];
        tickbox.checked = Number(level_data[level]["exits"][i]);
        var label = document.createElement("label");
        label.innerHTML = " - "+exitDir[i]+" ";
        label.setAttribute("for", "exit"+exitDir[i]);
        exits.append(label);
        exits.appendChild(tickbox)
    }
    explorer.appendChild(exits)
}


//REMINDER TO JDAVIS -- ADD SETTING VALUES YOU FUCKING IDIOT!!!
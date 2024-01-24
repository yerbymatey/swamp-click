//defining variables by locating them in the index.html file
const spawnAlgae = document.getElementById("spawnAlgae");
const spawnBugs = document.getElementById("spawnBugs");
const algaePopulationDisplay = document.getElementById("algae_population");
const bugPopulationDisplay = document.getElementById("bug_population");

//defining war store variables
const bugKillingStore = document.getElementById("bugKillingStore");
const algaeKillingStore = document.getElementById("algae KillingStore");

//assigning both pops to 0 at start
let populations = {
  algae: 0,
  bugs: 0,
};

//giving ability to iterate
let clickerCount = 0;
let clickMultiplier = 1;
//stages for war store
let algaeKillingMethods = [
  {
    name: "encapsulation",
    modifier: 0.9,
    multiplier: 1,
    operation: "multiply",
    population: "algae",
  },
  {
    name: "idk",
    modifier: 1.01,
    multiplier: 1,
    operation: "multiply",
    population: "algae",
  },
  {
    name: "swarm",
    modifier: 1.1,
    multiplier: 1,
    operation: "multiply",
    population: "algae",
  },
];
let item = {
  name: "encapsulation",
  modifier: 0.9,
  multiplier: 1,
  operation: "multiply",
  population: "algae",
};
function useItem(item, population) {
  if (item["operation"] == "multiply") {
    return population * (item["modifier"] * item["multiplier"]);
  }
}
function makeButton(item, storeId) {
  let newButton = document.createElement("button");
  // add name to button
  newButton.innerHTML = item["name"];
  //add button to page
  let store = document.getElementById(storeId);
  store.appendChild(newButton);
  newButton.addEventListener("click", function () {
    // get current population from item's pop key
    let currentPopulation = populations[item["population"]];
    //use item on correct pop
    populations[item["population"]] = useItem(item, currentPopulation);
    //update display with new pop
    const populationDisplay = document.getElementById( item["population"]+"_population");
    populationDisplay.innerHTML = populations[item["population"]]
  });
}
for (let i = 0; i < algaeKillingMethods.length; i++) {
  let item = algaeKillingMethods[i]
  makeButton(item, "algaeKillingStore")
}


let bugKillingMethods = ["pesticides", "taunt", "eat"];

//view controller 

spawnAlgae.addEventListener("click", function (event) {
  clickerCount += clickMultiplier;
  populations["algae"] += 1;
  console.log(clickerCount);
  algaePopulationDisplay.innerHTML = populations["algae"];
}); //listening to number of clicks of algae spawning

spawnBugs.addEventListener("click", function (event) {
  clickerCount += clickMultiplier;
  populations["bugs"] += 1;
  console.log(clickerCount);
  bugPopulationDisplay.innerHTML = populations["bugs"];
}); //listening to number of clicks of bugs spawning

//main loop
let timer = setInterval(function () {
  //war between algae and bugs, bugs eat algae, algae pop reproduces
  //algae reproduce double the algae population
  populations["algae"] *= 2;
  //bugs reduce algae population by number of bugs
  populations["algae"] -= populations["bugs"];
  //algae reduce bug population by number of algae
  populations["bugs"] -= populations["algae"];
  //bugs reproduce
  populations["bugs"] *= 2;
  console.log(populations)

  if (populations["algae"] >= 20000) {
    algaeKillingStore.innerHTML = algaeKillingStore;
  }
  if (populations["bugs"] >= 20000) {
    bugKillingStore.innerHTML = bugKillingStore;
  }
  //kill function if either population reaches 0
  if (populations["algae"] <= -1) {
    console.log("the f'ing bugs ate all the algae LOL");
    clearInterval(timer);
  } else if (populations["bugs"] <= -1) {
    console.log("algae rule the world");
    clearInterval(timer);
  }
  //updating populations of both bugs and algae
  algaePopulationDisplay.innerHTML = populations["algae"];
  bugPopulationDisplay.innerHTML = populations["bugs"];
}, 1000);

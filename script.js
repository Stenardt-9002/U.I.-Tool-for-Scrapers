const input = document.getElementById("url-input");
let state = false;
let isLoading = false;
// const displayArea = document.getElementById("display-area");
const displayArea = document.getElementById("container-1");

const loader = document.getElementById("loader-container");
const navs = document.querySelectorAll(".navs");

let URL = ""


let currentDisplay = "elements";




const pythonEditor = CodeMirror(document.getElementById("generation-area"), {
	// value: "from selenium import webdriver\nfrom selenium.webdriver.chrome.options import Options\n\n\nch = os.getcwd() + '/python/tools/chromedriver'\noptions = Options()\noptions.set_headless(headless=True)\noptions.add_argument('--disable-gpu')\noptions.add_argument('--disable-dev-shm-usage')\noptions.add_argument('--no-sandbox')\ndriver = webdriver.Chrome(options=options, executable_path=ch)",
	value: "from bs4 import BeautifulSoup,Comment\nimport requests\nimport re\nimport os \nimport time \n\n\n\n\n\n\ndef function_for_text(soup_obj,atrr):  \n    temp_tag = soup_obj.find_all(atrr[0],atrr[1])\n    string_data = \"\"    \n    for all_tags in temp_tag:\n        string_data+=str(all_tags.get_text())\n    return str(string_data)\n\n\n\n\n\n\n"     ,



	// # atrr = ["input",{"placeholder":"Search reviews"}]
	
	
	



	// +'''").text \nsoup = BeautifulSoup(html_stuff,"'''+ SOUP_PAR+'''")\nbody_tag = soup.body\n'''   + "options = Options()\noptions.set_headless(headless=True)\noptions.add_argument('--disable-gpu')\noptions.add_argument('--disable-dev-shm-usage')\noptions.add_argument('--no-sandbox')\ndriver = webdriver.Chrome(options=options, executable_path=ch)",

	mode: "python",
	lineNumbers: true,
	theme: "shadowfox"
});








// contains json file
let webContent = {
	"elements": 0,
	"tables": 0,
	"links": 0,
	"images": 0,
	"others": 0,
}

let buttonsText = [{
	"div": [
		"id='main'"
	],
},
{
	"p": [
		"class='text'",
		"This website is made for Test"
	],
},
{
	"h1": [
		"My Website"
	],
},
{
	"article": [
		"id='dummy'"
	]
},
];

// window.onload = () => {
// 	let empty = document.createElement("span");
// 	empty.innerText = "Enter URL to display elements";
// 	displayArea.appendChild(empty);
// 	displayArea.classList.add("empty");
// }



























const checkURL = (url) => {
	URL = url
	var urlPat = /^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$/
	if (urlPat.test(url) === false) {
		document.getElementById("status").style.visibility = "visible";
		state = false;
		return false;
	} else {
		document.getElementById("status").style.visibility = "hidden";
		state = true;
		return true;
	}
}



// const switchDisplay = (e) => {
// 	document.querySelector(`li[data-name=${currentDisplay}]`).classList.remove("hovered");
// 	let target = null;
// 	if (e.target.parentNode.className === "navs")
// 		target = e.target.parentNode;
// 	else
// 		target = e.target;
// 	currentDisplay = target.getAttribute("data-name");
// 	buttonsText = webContent[currentDisplay];
// 	renderButtons(buttonsText);
// 	target.classList.add("hovered");
// }



const submitURL = (e) => {
	if (e.keyCode === 13 && state) {


		isLoading = true;
		loader.style.display = "flex";

		console.log("DEbug1");

		var python = require('python-shell');
		// var python = python2;


		console.log("DEbug2");


		var options = {
			args: [URL, "github"],
			mode: 'json'
		}
		var script = new python.PythonShell('./python/main.py', options);



		script.on('message', (message) => {
			isLoading = false
			loader.style.display = "none";
			webContent = message;




			// const fs = require("fs");
			// // const users = require("./users");
			// // users.push(script);
	
			// // fs.writeFile("users.txt", JSON.stringify(users), err => {
			// fs.writeFile("users.txt",JSON.stringify(webContent) , err => {
	
		 
			// 	// Checking for errors
			// 	if (err) throw err; 
			   
			// 	console.log("Done writing"); // Success
			// });
	


			console.log("DEbug3");

			button_callback(URL,webContent)




			// buttonsText = webContent["elements"]
			// renderButtons(buttonsText);
			// navs[0].classList.add("hovered");
			// navs.forEach((nav) => {
			// 	nav.addEventListener("click", switchDisplay)
			// 	nav.childNodes[1].innerText = webContent[nav.getAttribute("data-name")].length
			// })
		})








		// if (isLoading)
		// 	loader.style.display = "none";

		console.log("DEbug4");


		// script.on('message', (message) => {
		// 	isLoading = false
		// 	loader.style.display = "none";
		// 	webContent = message;
		// 	buttonsText = webContent["elements"]
		// 	renderButtons(buttonsText);
		// 	navs[0].classList.add("hovered");
		// 	navs.forEach((nav) => {
		// 		nav.addEventListener("click", switchDisplay)
		// 		nav.childNodes[1].innerText = webContent[nav.getAttribute("data-name")].length
		// 	})
		// })
	}
}


input.addEventListener("input", () => checkURL(input.value));
input.addEventListener("keydown", submitURL);

























function selectButton(e) {
	var target = null;
	if (e.target.parentNode.className === "button" || e.target.parentNode.className === "button selected") {
		target = e.target.parentNode;
	} else if (e.target.parentNode.parentNode.className === "button" || e.target.parentNode.parentNode.className === "button selected") {
		target = e.target.parentNode.parentNode;
	} else if (e.target.className === "button" || e.target.className === "button selected") {
		target = e.target;
	}

	var x = target.innerText.split('\n')[1];
	var p = x.split("=")[1];
	var text = "\ndriver.find_element_by_xpath('" + p + "')";

}












function renderButtons(buttonsText) {

	while (displayArea.firstChild)
		displayArea.removeChild(displayArea.firstChild);
	displayArea.classList.remove("empty");

	for (var i = 0; i < buttonsText.length; i++) {
		var newButton = document.createElement("div");
		newButton.setAttribute("class", "button");

		var buttonHead = document.createElement("h2");
		buttonHead.setAttribute("class", "button-head");
		buttonHead.innerHTML = Object.keys(buttonsText[i]);
		newButton.appendChild(buttonHead);

		var buttonParaCon = document.createElement("div");
		buttonParaCon.setAttribute("class", "button-para-container");
		for (var j in buttonsText[i][Object.keys(buttonsText[i])]) {
			var buttonPara = document.createElement("p");
			buttonPara.setAttribute("class", "button-para");
			buttonPara.innerHTML = buttonsText[i][Object.keys(buttonsText[i])][j].slice(0, 35);
			buttonParaCon.appendChild(buttonPara);
		}
		newButton.appendChild(buttonParaCon);
		displayArea.appendChild(newButton);
		newButton.addEventListener("click", selectButton);
		if (isLoading)
			loader.style.display = "none";
	}
}



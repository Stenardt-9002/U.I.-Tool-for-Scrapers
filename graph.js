// ------ Global Variables ------ //
// const firstCode = require("./script.js")
// import {addCode} from "./script.js"
let gData = null;
let g2Data = null;
let gModel = null;
let G = null;

// ====== Graph Settings =======  //
let gContainer = null;
let gWidth = 650;
let gHeight = 850;
let nodeSize = 0.35;
let setNodeId = false;
let gDebug = false;

let ONCEDONE = 1;
function isValidUrl(string) {
    try {
      new URL(string);
    } catch (_) {
      return false;  
    }
  
    return true;
}

// function button_callback(){
//     let url = document.getElementById("url_p");

//     console.log('Button callback!!')
//     if (isValidUrl(url.value)){
        
//         console.log('Before AJAX!');
//         $.ajax({
//             url: "/json",
//             type: "get",
//             data: {jsdata: url.value},
//             success: function(response) {
//                 gData = null;
//                 manipulateData(response);
//             },
//             error: function(xhr) {
//                 //Do Something to handle error
//                 console.log('Error happened in AJAX call!');
//             }
//         });
//     }
//     else{
//         console.log(url.value + " is not valid!");
//     }    
// }  



function button_callback(url,response1)
{
    // if (isValidUrl(url)){
    //     manipulateData(response1);

    // }
    //     else{
    //     console.log(url + " is not valid!");
    // }  
        manipulateData(response1);

}  






function manipulateData(data){

    if (data == null){
        return;
    }

    // create node dictionary
    let ndict = {};
    let dictidtotag = {};

    data.nodes.forEach(function(node, index){
        ndict[node.id] = index;
        dictidtotag[index] = node.id ;
    });

    // Make links
    let links = data.links.map(function(link){
        src = ndict[link.source];
        target = ndict[link.target];
        return {"source" : src, "target" : target}
    });

    let model = {
        nodes: [],
        edges: []
    };

    data.nodes.forEach(function(node, n) {
        model.nodes.push({
        group: ( ('label' in node) ? node.label : 1),
        label: ( (setNodeId) ? node.id : null )
        });

    });

    links.forEach(function(link) {
        let fromIndex = link.source;
        let toIndex = link.target;

        model.edges.push({
        from: fromIndex,
        to: toIndex
        });
    });

    // =set model globally=
    gModel = model;
    
    // get radio buttons from UI
    var rd1=document.getElementById("rd1");
    var rd2=document.getElementById("rd2");
    var rd3=document.getElementById("rd3");
    var rd4=document.getElementById("rd4");

    // set container
    gContainer = document.getElementById("container-1");

    // set data globally
    gData = data;
    g2Data= dictidtotag;



    // const fs = require("fs");
    // fs.writeFile("users2.txt",JSON.stringify(g2Data) , err => {
    //      // Checking for errors
    //     if (err) throw err; 
       
    //     console.log("Done writing"); // Success
    // });


    // check radio buttons and render graph
    if(rd1.checked==true){ render_graph(ElGrapho.layouts.ForceDirected); }
    else if(rd2.checked==true){ render_graph(ElGrapho.layouts.Tree); }
    else if(rd3.checked==true){ render_graph(ElGrapho.layouts.RadialTree); }
    else if(rd4.checked==true){ render_graph(ElGrapho.layouts.Cluster); }
    
}

 function rd1_cf(){
     render_graph(ElGrapho.layouts.ForceDirected);
 }

 function rd2_cf(){
    render_graph(ElGrapho.layouts.Tree);
}

function rd3_cf(){
    render_graph(ElGrapho.layouts.RadialTree);
}

function rd4_cf(){
    render_graph(ElGrapho.layouts.Cluster);
}






// module.exports.addCode = function(e) {
function addCode(G1,indx1) {







	// var target = null;
	// if (e.target.parentNode.className === "button" || e.target.parentNode.className === "button selected") {
	// 	target = e.target.parentNode;
	// } else if (e.target.parentNode.parentNode.className === "button" || e.target.parentNode.parentNode.className === "button selected") {
	// 	target = e.target.parentNode.parentNode;
	// } else if (e.target.className === "button" || e.target.className === "button selected") {
	// 	target = e.target;
	// }

	// var x = target.innerText.split('\n')[1];
	// var p = x.split("=")[1];
	
    var btn = document.getElementById("toggle_button_code_p");

	if(ONCEDONE==1 && btn.checked )
    {

        var text = "html_stuff = requests.get(\""  +URL+  "\").text \nsoup = BeautifulSoup(html_stuff,\"lxml\")\nbody_tag = soup.body\n"
        pythonEditor.replaceRange(text, CodeMirror.Pos(pythonEditor.lastLine()));
        ONCEDONE = 0;
        }



        let node_id = gData.nodes[indx1].id;
        let name1d;
        console.log( "id",gData.nodes[indx1].id);
        let i = node_id.indexOf("_");
        if (i > -1){
            name1d = node_id.substring(0, i);
        // console.log("When Activate ")

    }
    else 
    {
        name1d = node_id;
    }


    console.log("Tag Name " ,name1d) ;

	console.log("attrs",  gData.nodes[indx1].attrs);
	// console.log("weary" , gData.nodes[indx1]);




    var text2 = "args1 = [\""+name1d +"\","+ JSON.stringify(gData.nodes[indx1].attrs) +"]\n\n" ;


    // console.log(gData.nodes[0]);
    // gData.nodes[indx1]

    // JSON.stringify(gData.nodes[index].attrs, null, 4) 


    // console.log(text2);

    text2 = text2+"try:\n    print(function_for_text(soup,args1))\nexcept:\n    print(\"Some Error occured\")\n\n\n\n";

    var btn = document.getElementById("toggle_button_code_p");
    if (btn.checked) 
    {
    	console.log("Toggle B1");
        pythonEditor.replaceRange(text2, CodeMirror.Pos(pythonEditor.lastLine()));

    }


}











function render_graph(layout){
    if (gModel == null){
        console.log('No model exists!')
        return;
    }
    // addCode(G);
    G = new ElGrapho({
        container: gContainer,
        model: layout(gModel),
        width: gWidth,
        height: gHeight,
        nodeSize: nodeSize,
        debug: gDebug
      });
    // set tooltip function
    G.tooltipTemplate = toolTipFn;
    // scroll to page bottom
    window.scrollTo(0,document.body.scrollHeight);


      //click and add information to editor 
      G.on('node-click', function(evt,ele) {
        console.log("When Activate ");
        console.log(evt);
        // console.log(ele);

        addCode(G,evt.dataIndex);
        // firstCode.addCode(G);
        // firstCode.selectButton(G);
        // selectButton(G);
      });


}


function toolTipFn(index, el) {
    // get node type from id
    let node_id = gData.nodes[index].id;
    // console.log(index);
    let i = node_id.indexOf("_");
    if (i > -1){
        node_id = node_id.substring(0, i);
    // console.log("When Activate ")

    }
    // el.innerHTML = node_id + "<br />" + "<pre>" + JSON.stringify(gData.nodes[index].attrs, null, 4) + "</pre>";
    el.innerHTML = node_id + "<br />" + "<pre>" + JSON.stringify(gData.nodes[index].attrs, null, 4) + "</pre>";
  
    // console.log(el);

};
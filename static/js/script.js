//generateNotes(5);

getNotes({"category":"category", "num_posts":20}, function(d){
	console.log("populate notes");
	console.log(d);
	data = d["result"];
	len = data.length;
	for (var i = 0; i<len; i++){
		var postit = JSON.parse(data[i]);
		console.log(postit);
		createPostIt(postit["title"],postit["content"], postit["category"]);
	}

});

function generateNotes(numNotes){

	for (var i=0; i<numNotes; i++){
		createPostIt();
	}

}

function createPostIt(title, content,category){
	$("#main").append("<div class='postit'>"+"<h2 class='title"+getRandomArbitrary(0,4)+"'>"+title+"</h2>"+
		"<div class='content'>"+ content + "</div>"+
		"<div class='category'>"+category+"</div>"+
		"</div>")
}

/**
 * Returns a random number between min (inclusive) and max (exclusive)
 */
function getRandomArbitrary(min, max) {
    return parseInt(Math.random() * (max - min) + min);
}

function dropDownInteractivity() {

    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].onclick = function() {
            this.classList.toggle("active");
            this.nextElementSibling.classList.toggle("show");
        }
    }
}

dropDownInteractivity();


/*---------------------ajax calls-------------------*/

var urlBase = window.location.hostname

$("#createNote").click(function(){
	data = {"title": "", "content":$("#noteContent").val(), "category":""}
	console.log(data);
	createNote(data);
})

function createNote(data) {
    $.ajax({
        type: 'POST',
        url: '/addNote',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        dataType: 'text',
        success: function(msg, status, jqXHR) {
            console.log(msg);
            alert("Submitted data");
        },
        error: function(jqXHR, textStatus, errorThrown) {
            alert(textStatus, errorThrown);
        }
    });
}


function getNotes(params, callback) {
    getData("/getNotes", params, callback);
}

function getData(urlBase=urlBase, params, callback) {
    var stringifiedParams = jQuery.param(params);
    url = urlBase + "?" + stringifiedParams;
    //console.log("Url: " + url);
    $.getJSON(url, function(json) {
        console.log("Url: " + url);
        callback(json);
    });
}

/*
function getNotes(data) {
    $.ajax({
        type: 'GET',
        url: '/getNotes',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        dataType: 'text',
        success: function(response) {
           console.log(response);
           result = response["result"];

        }
    });
}
*/

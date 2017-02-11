generateNotes(5);

getNotes({"category":"art", "num_posts":20}, function(d){
	console.log("populate notes");
	data = d["result"];

});

function generateNotes(numNotes){

	for (var i=0; i<numNotes; i++){
		createPostIt();
	}

}

function createPostIt(title, content){
	$("#main").append("<div class='postit'>"+"<h1>"+title+"</h1>"+
		"div class='content'>"+content + "</div>"+
		"</div>")
}



/*---------------------ajax calls-------------------*/

var urlBase = window.location.hostname

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
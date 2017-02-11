generateNotes(5);


function generateNotes(numNotes){
	for (var i=0; i<numNotes; i++){
		createPostIt();
	}

}

function createPostIt(){
	$("#main").append("<div class='postit'></div>")
}
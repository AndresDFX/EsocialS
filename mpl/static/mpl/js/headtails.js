var doneTheStuff;
jQuery(document).ready(function($){
$('#coin').on('click', function(){
    // $('#coin').removeClass();
    if (!doneTheStuff) {
        doneTheStuff = true;
    setTimeout(function(){
        console.log(flipResult);
    if(flipResult <= 0.5){
        $('#coin').addClass('heads');
        console.log('it is head');
    }
    else{
        $('#coin').addClass('tails');
        console.log('it is tails');
    }
    }, 100);
}
}
);
});

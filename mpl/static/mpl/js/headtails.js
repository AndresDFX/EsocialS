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
    // $('#coin').removeClass();
    // $('#heads').removeClass();
    // $('#tails').removeClass();
    // $('#side-a').removeClass();
    // $('#side-b').removeClass();
    // document.getElementById('coin').onclick = () => false; 
    // document.getElementById('side-a').onclick = () => false; 
    // document.getElementById('side-b').onclick = () => false; 
    // document.getElementById('heads').onclick = () => false; 
    // document.getElementById('tails').onclick = () => false; 
}
}
);
});

$(document).ready(function(){
    $(".read").click(function(){
       $(this).prev().toggle();
       $(this).siblings('.dots').toggle();
       if($(this).text()=='Read less'){
     $(this).text('Read more');
       }
       else{
     $(this).text('Read less');
       }
    });
 });
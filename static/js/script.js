$('#keyword').keyup(function() {
    var title = $('#keyword').val();
    var sumber_url = 'https://www.googleapis.com/books/v1/volumes?q=' + title;
    console.log(sumber_url)
    $.ajax({
        url: sumber_url,
        success:function(result) {
            console.log(result.items)
            var res = $('#res');
            res.empty();

            for (i = 0; i < result.items.length; i++) {
                var titles = result.items[i].volumeInfo.title;
                var imge = result.items[i].volumeInfo.imageLinks.smallThumbnail;
                var author = result.items[i].volumeInfo.authors;
                var desc = result.items[i].volumeInfo.description;
                if (desc == "undefined")
                    desc = "no description available";
                console.log(titles);
                console.log(desc);
                res.append(
                    "<div class=" + "row container" + "style:'padding: 2% 0% 2%; width:max-width;'>" +  
                        "<div class=" + "col-md-4" + ">" + (i+1) + ".   " + "<img src=" + imge + "></div>" +
                        "<div class=" + "col-md-8" + ">" + "<b style='font-size: larger;'>" + titles + "</b>" + "<br>" +
                        "<b class=" + "book-author" + ">" + author + "</b>" + "<br>" + desc + "</div></div>" 




                   );
            }
        }
        
    });
});
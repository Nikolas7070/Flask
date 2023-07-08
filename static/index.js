function showContainer(event) {
            var element = event.target.nextElementSibling;
            element.style.visibility = 'visible';
        }

        function hideContainer(event) {
            var element = event.target.nextElementSibling;
            element.style.visibility = 'hidden';
        }

        window.addEventListener('DOMContentLoaded', function () {
            var word1Elements = document.getElementsByClassName('word1');
            for (var i = 0; i < word1Elements.length; i++) {
                word1Elements[i].addEventListener('mouseenter', showContainer);
                word1Elements[i].addEventListener('mouseleave', hideContainer);
            }
        });
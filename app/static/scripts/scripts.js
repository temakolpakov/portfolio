$(document).ready(function () {
    // Add smooth scrolling to all links
    $("a").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();

            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function () {
                window.location.hash = hash;
            });
        }
    });
});

$(document).ready(function () {
    // Open project modal when the "View Details" button is clicked
    $('.card button').on('click', function () {
        var targetModal = $($(this).data('target'));
        targetModal.modal('show');
    });

    // Close project modal when the modal is closed
    $('.modal').on('hidden.bs.modal', function () {
        $(this).find('iframe').attr('src', $(this).find('iframe').attr('src'));
    });
    // Open project modal when the project card is clicked
    $('.card').on('click', function () {
        var targetModal = $($(this).find('button').data('target'));
        targetModal.modal('show');
    });

    // Close project modal when the modal is closed
    $('.modal').on('hidden.bs.modal', function () {
        $(this).find('iframe').attr('src', $(this).find('iframe').attr('src'));
    });
});
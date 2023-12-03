let selectedSlice = null;

    function selectSlice(sliceNumber) {
        // Remove 'selected' class from all labels
        document.querySelectorAll('.btn').forEach(label => {
        label.classList.remove('selected');
        });

        // Add 'selected' class to the clicked label
        document.querySelector(`[onclick="selectSlice(${sliceNumber})"]`).classList.add('selected');

        selectedSlice = sliceNumber;

        // You can perform additional actions here if needed

        // Example: Display the selected slice number
        console.log('Selected slice:', selectedSlice);
    }
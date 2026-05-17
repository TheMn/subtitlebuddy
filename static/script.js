document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = document.getElementById('mediaFile');
    const fileNameDisplay = document.getElementById('fileNameDisplay');
    const submitBtn = document.getElementById('submitBtn');
    const statusMessage = document.getElementById('statusMessage');
    const successMessage = document.getElementById('successMessage');
    const errorMessage = document.getElementById('errorMessage');

    // Update file name display when a file is selected
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            fileNameDisplay.textContent = e.target.files[0].name;
            fileNameDisplay.style.color = 'var(--text-color)';
        } else {
            fileNameDisplay.textContent = 'Choose a file...';
            fileNameDisplay.style.color = 'var(--text-muted)';
        }
    });

    uploadForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const file = fileInput.files[0];
        if (!file) return;

        // Reset UI states
        successMessage.classList.add('hidden');
        errorMessage.classList.add('hidden');
        statusMessage.classList.remove('hidden');
        submitBtn.disabled = true;

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            // Get the filename from the Content-Disposition header if possible
            let filename = `${file.name.split('.')[0]}.srt`;
            const disposition = response.headers.get('Content-Disposition');
            if (disposition && disposition.indexOf('attachment') !== -1) {
                const filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
                const matches = filenameRegex.exec(disposition);
                if (matches != null && matches[1]) {
                    filename = matches[1].replace(/['"]/g, '');
                }
            }

            // Trigger file download
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();

            // Cleanup
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);

            // Show success
            statusMessage.classList.add('hidden');
            successMessage.classList.remove('hidden');

            // Reset form
            uploadForm.reset();
            fileNameDisplay.textContent = 'Choose a file...';
            fileNameDisplay.style.color = 'var(--text-muted)';

        } catch (error) {
            console.error('Upload failed:', error);
            statusMessage.classList.add('hidden');
            errorMessage.classList.remove('hidden');
        } finally {
            submitBtn.disabled = false;
        }
    });
});

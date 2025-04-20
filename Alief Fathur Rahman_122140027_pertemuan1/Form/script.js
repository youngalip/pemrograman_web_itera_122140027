document.addEventListener("DOMContentLoaded", function () {
    function validateForm() {
        let name = document.getElementById("name").value;
        let email = document.getElementById("email").value;
        let password = document.getElementById("password").value;
        
        let nameError = document.getElementById("nameError");
        let emailError = document.getElementById("emailError");
        let passwordError = document.getElementById("passwordError");

        let isValid = true;

        // Validasi Nama (Minimal 3 karakter)
        if (name.length < 3) {
            nameError.textContent = "Nama harus lebih dari 3 karakter";
            isValid = false;
        } else {
            nameError.textContent = "";
        }

        // Validasi Email (Format email)
        let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!email.match(emailPattern)) {
            emailError.textContent = "Email tidak valid";
            isValid = false;
        } else {
            emailError.textContent = "";
        }

        // Validasi Password (Minimal 8 karakter)
        if (password.length < 8) {
            passwordError.textContent = "Password harus minimal 8 karakter";
            isValid = false;
        } else {
            passwordError.textContent = "";
        }

        return isValid;
    }

    // Fitur "Tampilkan Password"
    function togglePassword() {
        let passwordField = document.getElementById("password");
        let toggleIcon = document.querySelector(".toggle-password");

        if (passwordField.type === "password") {
            passwordField.type = "text";
            toggleIcon.textContent = "🙈"; // Ubah ikon ke mata tertutup
        } else {
            passwordField.type = "password";
            toggleIcon.textContent = "👁️"; // Ubah ikon ke mata terbuka
        }
    }

    // Tambahkan fungsi ke global scope agar bisa dipanggil dari HTML
    window.validateForm = validateForm;
    window.togglePassword = togglePassword;
});

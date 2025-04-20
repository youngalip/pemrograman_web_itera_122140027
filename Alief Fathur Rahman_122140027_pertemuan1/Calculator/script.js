function appendValue(value) {
    document.getElementById("display").value += value;
}

function clearDisplay() {
    document.getElementById("display").value = "";
}

function backspace() {
    let display = document.getElementById("display").value;
    document.getElementById("display").value = display.slice(0, -1);
}

function calculate() {
    let expression = document.getElementById("display").value;

    try {
        if (expression.includes("^")) {
            let [base, exponent] = expression.split("^").map(Number);
            document.getElementById("display").value = Math.pow(base, exponent);
        } else if (expression.includes("√")) {
            let number = parseFloat(expression.replace("√", ""));
            if (number >= 0) {
                document.getElementById("display").value = Math.sqrt(number);
            } else {
                throw new Error("Tidak bisa menghitung akar dari angka negatif!");
            }
        } else if (expression.includes("%")) {
            let [num1, num2] = expression.split("%").map(Number);
            document.getElementById("display").value = num1 % num2;
        } else {
            document.getElementById("display").value = eval(expression);
        }
    } catch (error) {
        document.getElementById("display").value = "Error!";
    }
}

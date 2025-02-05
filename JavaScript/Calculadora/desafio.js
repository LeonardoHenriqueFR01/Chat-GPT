// Crie uma calculadora que receba 3 argumentos n1, n2 e o operador

function calculadora(n1, n2, operador) {
    
    if (operador === "+") {
        console.log(`${n1} + ${n2} = ${n1 + n2}`)
    
    } else if (operador === "-") {
        console.log(`${n1} - ${n2} = ${n1 - n2}`)
    
    } else if (operador === "*") {
        console.log(`${n1} x ${n2} = ${n1 * n2}`)
   
    } else if (operador === "/") {
        if (n1 === 0 || n2 === 0) {
            console.log(`Não é possível fazer divisão por zero.`)
        } else {
            console.log(`${n1} / ${n2} = ${n1 / n2}`)
        }
   
    } else if (operador === "%") {
        console.log(`${n1} % ${n2} = ${n1 % n2}`)
    }
}


calculadora(5, 5, "*")

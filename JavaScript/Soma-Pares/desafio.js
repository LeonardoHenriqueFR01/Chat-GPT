function somaPares() {
    var soma_1 = 0;
    var soma_2 = 0;

    var numeros_1 = [1, 2, 3, 4, 5, 6];
    var numeros_2 = [10, 15, 20, 25];

    for (let i = 0; i < numeros_1.length; i++) {
        if (numeros_1[i] % 2 === 0) {
            soma_1 += numeros_1[i];  // Adiciona diretamente à soma
        } 
    }
    console.log(soma_1);

    for (let i = 0; i < numeros_2.length; i++) {
        if (numeros_2[i] % 2 === 0) {
            soma_2 += numeros_2[i];  // Adiciona diretamente à soma
        }
    }
    console.log(soma_2);
}

somaPares();

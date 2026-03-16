// Your task is to write function factorial.

function factorial(n) {
    if (n === 0) { return 1; }
    let out = n;
    while (n > 1) {
        out *= (--n);
    }
    return out;
}
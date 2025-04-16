// yh fn = n * n-1 * n-2 till n=n-1
function factorial(n) {
  if (n === 1) {
    return n
  }

  return n * factorial(n-1)
}

// 5 * fn(5-1) | 4 * fn(4-1) | 3 * fn(3-1) | 2 * fn(2-1) | 1 * 1 
// 1*2 | 1*2*3 | 1*2*3*4 | 1*2*3*4*5
// const test1 = factorial(5)
// const test2 = factorial(100)

function fib(n) {
  if ( n <= 1) {
    return n
  }

  return fib(n-1) + fib(n-2)
}


function exponential(n, exp) {
  if ( exp <= 1) {
    return n
  }

  return n * exponential(n , (exp-1))
}

function naturalNumbers(n) {
  if (n <=1) {
    return n
  }

  return n + naturalNumbers(n-1)
}


function hanoiTowers(n) {

}

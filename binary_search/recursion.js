// console.log(Math.floor(5/2))

function binaryConversion(number) {
  if (number === 0 || Math.floor(number/2) === 0) {
    return number 
  }

  const remainder = number % 2
  const wholeNumber = Math.floor(number/2)
  console.log(wholeNumber, "-->", remainder)

  return binaryConversion(wholeNumber) + `${remainder}`
}
// const binary = binaryConversion(233)
// console.log(binary)

function sumOfNaturalNumbers(n) {
  if (n == 1 || n-1 === 0) {
    return n 
  }

  let currNumber = n - 1 
  let newSum = currNumber + n
  console.log("passedInValueOfN --> ",n, "ReductionofN-->", currNumber, "--->newSum", newSum)

  return sumOfNaturalNumbers(currNumber) + n 
}

const sum = sumOfNaturalNumbers(10)
console.log(sum)



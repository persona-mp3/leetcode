function reverseString(word) {
  if (word.trim() === "") {
    return ""
  }

  // subString returns a new string starting at the index specified 
  return reverseString(word.substring(1)) + word.charAt(0)
}
// const reversedStr = reverseString("hello")
// console.log(reversedStr)
//
function isPalindrome(word){

  if (word.length === 0 || word.length === 1) {
    return true
  }

  if (word.charAt(0) === word.charAt(word.length - 1)){
    return isPalindrome(word.substring(1, word.length - 1))
  }

  false
}

const racecar = isPalindrome("racecar")
console.log(racecar)

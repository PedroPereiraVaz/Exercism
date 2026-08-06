//
// This is only a SKELETON file for the 'Line Up' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const format = (name, number) => {
  let end = "th"
  const last_digit = number%10
  const before_digit = number %100
  
  if (last_digit == 1 && before_digit != 11){
    end = "st"
  }
  if (last_digit == 2 && before_digit != 12){
    end = "nd"
  }
  if (last_digit == 3 && before_digit != 13){
    end = "rd"
  }
  
  let message = `${name}, you are the ${number}${end} customer we serve today. Thank you!`
  return message
};

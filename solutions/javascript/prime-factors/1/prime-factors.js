//
// This is only a SKELETON file for the 'Prime Factors' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const primeFactors = (n) => {
  const primes = [];
  let divisor = 2;
  while (n > 1) {
    while (n % divisor === 0) {
      primes.push(divisor);
      n /= divisor;
    }
    divisor++;
  }
  return primes;
};

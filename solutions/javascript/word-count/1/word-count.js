//
//  Separators: : ! ? \t \n \s
//

export const countWords = (text) => {
  const countWords = {};
  const words = text.replace(/[&@$%^]/g, "").split(/[:!?\t\n\s,. ]+/g);
  words.forEach((w) => {
    const word = w.replace(/^'+|'+$/g, "").toLowerCase();
    if (!word) return;
    countWords[word] = (countWords[word] ?? 0) + 1;
  });
  return countWords;
};

console.log(countWords("Joe can't tell between 'large' and large."));

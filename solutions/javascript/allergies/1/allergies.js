//
// This is only a SKELETON file for the 'Allergies' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const ALERGIES = [
  "eggs",
  "peanuts",
  "shellfish",
  "strawberries",
  "tomatoes",
  "chocolate",
  "pollen",
  "cats",
];

export class Allergies {
  constructor(alergias) {
    this.listAlergias = [];
    for (let i = 0; i < ALERGIES.length; i++) {
      if (Number(alergias) & (1 << i)) this.listAlergias.push(ALERGIES[i]);
    }
  }

  list() {
    return this.listAlergias;
  }

  allergicTo(alergie) {
    return this.listAlergias.includes(alergie);
  }
}

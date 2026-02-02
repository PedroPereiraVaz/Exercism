//
// This is only a SKELETON file for the 'List Ops' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class List {
  constructor(values = []) {
    this.values = values || [];
  }

  append(list) {
    this.values = [...this.values, ...list.values];
    return this;
  }

  concat(listOfLists) {
    const newList = new List(this.values);
    listOfLists.values.forEach((list) => newList.append(list));
    return newList;
  }

  filter(fn) {
    const filtered = [];
    for (const val of this.values) if (fn(val)) filtered.push(val);
    return new List(filtered);
  }

  map(fn) {
    const mapped = [];
    for (const val of this.values) mapped.push(fn(val));
    return new List(mapped);
  }

  length() {
    let len = 0;
    for (let _ of this.values) len++;
    return len;
  }

  foldl(fn, ac) {
    for (let elemento of this.values) ac = fn(ac, elemento);
    return ac;
  }

  foldr(fn, ac) {
    for (let i = this.length() - 1; i >= 0; i--) ac = fn(ac, this.values[i]);
    return ac;
  }

  reverse() {
    let reverseList = new List();
    for (let i = this.length() - 1; i >= 0; i--) {
      reverseList = reverseList.append(new List([this.values[i]]));
    }
    return reverseList;
  }
}

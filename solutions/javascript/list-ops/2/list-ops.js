//
// This is only a SKELETON file for the 'List Ops' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class List {
  constructor(values = []) {
    this.values = values || [];
  }

  append(list) {
    return new List([...this.values, ...list.values]);
  }

  concat(arrLists) {
    let concatList = new List(this.values);
    if (arrLists.length() > 0) {
      for (let list of arrLists.values) {
        concatList = concatList.append(list);
      }
    }

    return concatList;
  }

  filter(fn) {
    let filterList = new List();
    for (let elemento of this.values)
      if (fn(elemento)) filterList = filterList.append(new List([elemento]));
    return filterList;
  }

  map(fn) {
    let mapList = new List();
    for (let elemento of this.values)
      mapList = mapList.append(new List([fn(elemento)]));
    return mapList;
  }

  length() {
    let len = 0;
    for (let x of this.values) len++;
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

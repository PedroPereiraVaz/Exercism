export class Cipher {
  constructor(key) {
    this._key = key ?? Cipher.randomKey();
  }

  static randomKey(len = 100) {
    return Array.from({ length: len }, () =>
      String.fromCharCode(97 + Math.floor(Math.random() * 26))
    ).join('');
  }

  process(text, dir) {
    return [...text].map((ch, i) => {
      const shift = this._key.charCodeAt(i % this._key.length) - 97;
      const code = ch.charCodeAt(0) - 97;
      return String.fromCharCode(((code + dir * shift + 26) % 26) + 97);
    }).join('');
  }

  encode(txt) { return this.process(txt, +1); }
  decode(txt) { return this.process(txt, -1); }

  get key() { return this._key; }
  set key(v) { this._key = v; }
}

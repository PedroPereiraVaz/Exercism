//
// This is only a SKELETON file for the 'Conway's Game of Life' exercise. It's been provided
// as a convenience to get you started writing code faster.
//
const MOVES = [[-1, -1],[-1, 0],[-1, 1],[0, -1],[0, 1],[1, -1],[1, 0],[1, 1],];
export class GameOfLife {
  #m
  constructor(m) {
    this.#m = m;
  }

  tick() {
    const newState = this.#m.map((row) => [...row]);
    for (let x = 0; x < this.#m.length; x++) {
      for (let y = 0; y < this.#m[x].length; y++) {
        const neighbors = MOVES.reduce((sum, [dx, dy]) => sum + (this.#m[x + dx]?.[y + dy] ?? 0),0);
        newState[x][y] = Number(neighbors === 3 || (this.#m[x][y] === 1 && neighbors === 2));
      }
    }
    this.#m = newState;
  }
  state = () => this.#m;
}

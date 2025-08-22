// 5-building.js
export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') throw new TypeError('sqft must be a number');
    this._sqft = sqft;

    if (this.constructor !== Building
      && this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  /* eslint class-methods-use-this: ["off"] */
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}

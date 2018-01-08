import { freezeMerge } from './utils'

export default class Store {

  constructor(initialState = {}) {
    this._state = initialState
  }

  setState(key, nextState) {
    if (key && typeof nextState === 'undefined') {
      this._state = freezeMerge({}, this._state, key)
    } else {
      this._state[key] = freezeMerge({}, this._state, nextState)
    }
  }

  getState(key) {
    return key ? this._state[key] : this._state
  }

}

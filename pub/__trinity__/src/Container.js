import roadtrip from 'roadtrip'
import { Base } from 'selfish'

import { freezeMerge, findElem, getElement } from './utils'


const Container = Base.extend({
  initialize(props) {
    this._linkEventListeners = []
    this._eventListeners = []

    this.props = props
    //this._prefetch(props)
  },

  setState(nextState) {
    this.state = freezeMerge({}, this.state, nextState)
    this._triggerRender()

    return this.state
  },

  _setProps(nextProps) {
    this.props = freezeMerge({}, this.props, nextProps)

    return this.props
  },

  _setup(nextProps) {
    this._setProps(nextProps)

    this.state = Object.freeze(
      this.getInitialState && this.getInitialState(this.props) || {}
    )

    return this
  },

  _prefetch(props) {
    this._setProps(props)

    return new Promise((resolve, reject) => {
      if (typeof this.beforeMount === 'function') {
        const options = this.beforeMount(this.props)

        if (typeof options.action === 'function') {
          this._elementRender(options.selector || this.parent, options.html)

          options.action(this.props).then(result => {
            console.log(result)

            resolve()
          }).catch(reject)
        } else {
          throw new TypeError(`beforeMount.action is not a Promise`)
        }
      } else {
        resolve()
      }
    })
  },

  _triggerRender() {
    const { props, state, render } = this

    const { html, selector } = render({ props, state })

    return this._elementRender(selector || props.parent, html, !!this.parent)
  },

  _addEventListeners(el) {
    const { props, _eventListeners } = this

    const componentEvents = typeof this.events === 'function' && this.events() || []

    componentEvents.forEach(({ preventDefault, useCapture, handler, action, selector }) => {
      const element = findElem(selector)

      if (element) {
        const listener = (event) => {
          if (preventDefault) event.preventDefault()

          return action({ props, event })
        }

        element.addEventListener(handler, listener, useCapture)
      }
    })
  },

  _navigateListeners(parent) {
    const tag = '[data-navigate]'

    //parent.getElementsByTagName(tag)
    parent.querySelectorAll(tag).forEach(element => {
      element.addEventListener('click', (event) => {
        event.preventDefault()

        console.log('CLICK')

        const url = element.getAttribute('href')
        const attr = element.getAttribute(tag)

        if (['replaceState', 'invisible'].includes(attr)) {
          roadtrip.goto(url, { [attr]: true })
        } else {
          roadtrip.goto(url)
        }
      })
    })
  },

  _removeEventListeners() {
    this._eventListeners.forEach((event, i) => {
      event.element.removeEventListener(event.handler, event.listener)
      this._eventListeners.splice(i, 1)
    })

    return this
  },

  _elementRender(element, html) {
    const el = getElement(element)

    console.log(el)

    el.innerHTML = html//this.filterHTML(html)

    this._addEventListeners(el)
    this._navigateListeners(el)

    return el
  }

})

export default Container
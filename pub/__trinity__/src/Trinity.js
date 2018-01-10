import roadtrip from 'roadtrip'

import ContainerController from './ContainerController'
import Store from './Store'
import ApiClient from './ApiClient'

export default class Trinity {

  constructor(parent, api, store) {
    this.controllers = {}
    this.parent = parent
    this.store = new Store(store)
    this.api = new ApiClient(api)
  }

  add(route, component, ...canEnter) {
    //this.routes.push({ route, component })

    this.handleRouteComponent(route, component, ...canEnter)

    return this
  }

  validateEnters(enters) {
    const validations = []

    enters.forEach(enter => {
      const state = this.store.getState()

      const canEnter = enter.selector(state)

      validations.push(canEnter)

      if (!canEnter) {
        this.redirect(enter.redirect)
      }
    })

    return validations.every(val => !!val)
  }

  handleRouteComponent(routeName, container, ...enters) {
    roadtrip.add(routeName, {
      enter: (route, previousRoute) => {
        if (this.validateEnters(enters)) {
          this.controllers[routeName] = new ContainerController(container, this.parent, this.store, this.api)

          const render = () => this.controllers[routeName].container._triggerRender()

          this.controllers[routeName].container._prefetch({ route, previousRoute })
            .then(render)
            .catch(render)
        }
      },
      update: (route, previousRoute) => {
        const { container } = this.controllers[routeName]

        container._setProps({ route, previousRoute })
        container._triggerRender()
      },
      leave: (route, nextRoute) => {
        if (this.validateEnters(enters)) {
          this.controllers[routeName].willLeave({ route, nextRoute })
        }
      }
    })
  }

  redirect = (path) => this.navigate(path, { replaceState: true })

  navigate = (...args) => roadtrip.goto(...args)

  start = () => roadtrip.start()

}

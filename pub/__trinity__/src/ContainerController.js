export default class ContainerController {

  constructor(Container, parent, store, api) {
    this.container = new Container({ parent, api, store })

    this.container._setup({})
  }

  willLeave(nextProps) {
    if (this.container.routeWillLeave instanceof Function) {
      const props = this.container._setProps(nextProps)

      this.container.routeWillLeave(props)
    }
  }

}

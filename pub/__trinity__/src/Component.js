import Container from './Container'

const Component = Container.extend({
  initialize(props) {

    const id = Math.random().toString(36).slice(-5)

    const parent = document.createElement('div')
    parent.setAttribute('id', id)

    this.parent = parent

    console.log(id)

    Container.prototype.initialize.call(this, props)
  }
})

export default Component
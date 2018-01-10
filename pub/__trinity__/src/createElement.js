import { getComponentDisplayName, htmlToElement, cloneNodeSetHTML, findById } from './utils'

const elements = {}

//isEqualNode
//isSameNode

export default function createElement(Component, props) {
  const component = new Component(props)

  component._setup({})

  const name = getComponentDisplayName(component)
  const getHtmlNode = () => {
    const html = component.render({ props }).html

    if (component.parent) {
      return cloneNodeSetHTML(component.parent, html)
    }

    return htmlToElement(html)
  }

  const currentNode = getHtmlNode()

  if (!elements.hasOwnProperty(name)) {
    elements[name] = { didPrefetch: false, node: currentNode }
  }

  const shouldPrefetch = !elements[name].didPrefetch && typeof component.beforeMount === 'function'

  const oldNodeCopy = htmlToElement(elements[name].node.innerHTML)
  const currentNodeCopy = htmlToElement(currentNode.innerHTML)
  const currentNodeEqualsOld = oldNodeCopy.isEqualNode(currentNodeCopy)

  const triggerElementRender = (nextNode) => {
    const elemInterval = window.setInterval(() => {
      window.clearInterval(elemInterval)

      const render = () => {
        elements[name] = { didPrefetch: true, node: currentNode }

        component._elementRender(component.parent, currentNode.innerHTML)
      }

      if (shouldPrefetch) {
        component._prefetch(props)
          .then(render)
          .catch(render)
      } else {
        render()
      }
    }, 50)

    const beforeMountNode = cloneNodeSetHTML(component.parent, component.beforeMount(props).html)

    return shouldPrefetch ? beforeMountNode.outerHTML : nextNode.outerHTML
  }

  if (shouldPrefetch) {
    return triggerElementRender(elements[name].node)
  } else if (!currentNodeEqualsOld) {
    return triggerElementRender(currentNode)
  }

  return elements[name].node.outerHTML
}
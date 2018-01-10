import merge from 'lodash.merge'

export const freezeMerge = (...args) => Object.freeze(merge(...args))

export const getComponentDisplayName = (component) => {
  return component.displayName || component.name || component.toString()
}

export const findElem = (selector) => document.querySelector(selector)

export const findById = (id) => document.getElementById(id)

export const htmlToElement = (html) => {
  const template = document.createElement('template')
  template.innerHTML = html
  return template.content.firstElementChild
}

export const cloneNodeSetHTML = (node, html) => {
  const newNode = node.cloneNode(true)
  newNode.innerHTML = html

  return newNode
}

export const getElement = (element) => {
  return typeof element === 'object' && element.nodeType ? findById(element.id) : findElem(element)
}

export const nodeExistsInDom = (node) => document.body.contains(node)
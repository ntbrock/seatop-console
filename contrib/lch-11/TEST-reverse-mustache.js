var reverseMustache = require('reverse-mustache');
var result = reverseMustache({
  template: 'hello {{#place}}world{{/place}}',
  content: 'hello world'
});
console.log(result);

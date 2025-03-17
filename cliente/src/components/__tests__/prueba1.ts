import { mount } from '@vue/test-utils';
//import MyComponent from '@/components/MyComponent.vue';

describe('MyComponent.vue', () => {
  it('renders the correct message', () => {

    expect("Algo").toContain('Hola, Luis!');
  });
});

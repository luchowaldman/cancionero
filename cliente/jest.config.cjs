module.exports = {
    preset: 'ts-jest',
    testEnvironment: 'jsdom',
    moduleFileExtensions: ['js', 'json', 'jsx', 'ts', 'tsx', 'vue'],
    transform: {
      '^.+\\.vue$': '@vue/vue3-jest',
      '^.+\\.(ts|js)$': 'ts-jest',
    },
    moduleNameMapper: {
      '^@/(.*)$': '<rootDir>/src/$1',
    },
  };
  
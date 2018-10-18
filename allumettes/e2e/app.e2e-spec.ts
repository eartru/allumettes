import { AllumettesPage } from './app.po';

describe('allumettes App', function() {
  let page: AllumettesPage;

  beforeEach(() => {
    page = new AllumettesPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});

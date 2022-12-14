import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SnapFaceTutorialComponent } from './snap-face-tutorial.component';

describe('SnapFaceTutorialComponent', () => {
  let component: SnapFaceTutorialComponent;
  let fixture: ComponentFixture<SnapFaceTutorialComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SnapFaceTutorialComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SnapFaceTutorialComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PersonalReportsComponent } from './personal-reports.component';

describe('PersonalReportsComponent', () => {
  let component: PersonalReportsComponent;
  let fixture: ComponentFixture<PersonalReportsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PersonalReportsComponent]
    });
    fixture = TestBed.createComponent(PersonalReportsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

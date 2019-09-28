/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { SyncRhythemService } from './SyncRhythem.service';

describe('Service: SyncRhythem', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SyncRhythemService]
    });
  });

  it('should ...', inject([SyncRhythemService], (service: SyncRhythemService) => {
    expect(service).toBeTruthy();
  }));
});

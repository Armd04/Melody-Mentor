import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent {

  public constructor(private router: Router) {
    this.passwordIsShow = `password`;
  }

  public passwordIsShow: string;


  public changePasswordState() {
    if (this.passwordIsShow == `password`) {
      this.passwordIsShow = `text`;
    } else {
      this.passwordIsShow = `password`;
    }
  }
}

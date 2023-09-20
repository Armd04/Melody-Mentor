import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  translate: any;
  cookieService: any;
  public constructor(private router: Router) {
    this.submitted = false;
    localStorage.removeItem('id_token');
    this.passwordIsShow = `password`;
  }



  public passwordIsShow: string;
  public submitted: boolean;
  public login: any;
  public loginResponse?: any;

  public thisCulture: any;

  public ngOnInit() { }

  public onSubmit(): void {
    this.submitted = true;

    // this.loginService.getToken(this.login)
    //   .subscribe(
    //     result => {
    //       if (result.token == `UNAUTHORIZED`) {
    //         this.messageService.add(`نام‌کاربری و یا رمز‌عبور اشتباه است`)
    //         this.messageService.addinfo(result);
    //       } else {
    //         this.loginResponse = result;
    //         localStorage.setItem('id_token', this.loginResponse.token);
    //         this.router.navigate(["home"]);
    //       }
    //       this.submitted = false;
    //     },
    //     error => {
    //       if (error.status == 500 && error.error.status == 500) {
    //         this.messageService.add(`نام‌کاربری و یا رمز‌عبور اشتباه است`)
    //       }
    //       this.messageService.addinfo(error);
    //       this.submitted = false;
    //     },
    //     () => {
    //       console.log(`Completed!`);
    //     }
    //   );
  }

  public changePasswordState() {
    if (this.passwordIsShow == `password`) {
      this.passwordIsShow = `text`;
    } else {
      this.passwordIsShow = `password`;
    }
  }
}

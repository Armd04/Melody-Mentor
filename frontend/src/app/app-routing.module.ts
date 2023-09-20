import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LayoutComponent } from './layouts/layout/layout.component';
import { LoginComponent } from './dashboard/pages/login/login.component';
import { SignUpComponent } from './dashboard/pages/sign-up/sign-up.component';
import { LoggedInLayoutComponent } from './layouts/logged-in-layout/logged-in-layout.component';
import { ContactUsComponent } from './dashboard/pages/contact-us/contact-us.component';

const routes: Routes = [
  {
    path: '',
    component: LayoutComponent,
    children: [
      {
        path: 'login',
        title: 'ورود',
        component: LoginComponent
      },
      {
        path: 'register',
        title: 'ثبت نام',
        component: SignUpComponent,
      },
      {
        path: 'contact-us',
        title: 'ارتباط با ما',
        component: ContactUsComponent,
      },
      {
        path: '**',
        redirectTo: '/login',
        pathMatch: 'full',
      },
    ]
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

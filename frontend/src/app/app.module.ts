import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoggedInLayoutComponent } from './layouts/logged-in-layout/logged-in-layout.component';
import { LayoutComponent } from './layouts/layout/layout.component';
import { LoginComponent } from './dashboard/pages/login/login.component';
import { SignUpComponent } from './dashboard/pages/sign-up/sign-up.component';
import { ContactUsComponent } from './dashboard/pages/contact-us/contact-us.component';

@NgModule({
  declarations: [
    AppComponent,
    LoggedInLayoutComponent,
    LayoutComponent,
    LoginComponent,
    SignUpComponent,
    ContactUsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
